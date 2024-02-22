import json
import pdfkit
import random
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from rail_ticket_application.models import Train, Ticket_details


# Create your views here.

def home(request):
    print("Method is", request.method)
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        # return HttpResponse("insert data into DB")
        n = request.POST['name']
        print("Name is", n)
    return HttpResponse("Values fetched successfully")


def search(request):
    context = {}
    fromStation = request.GET['fromStn']
    toStation = request.GET['toStn']
    j = request.GET['journeyDate']
    if fromStation == "" or toStation == "" or j == "":
        context['Errormsg'] = "Field cannot be empty"
        return render(request, 'index.html', context)
    q1 = Q(source=fromStation)
    q2 = Q(destination=toStation)
    q3 = Q(journeyDate=j)
    t = Train.objects.filter(q1 & q2 & q3)

    if t.exists():
        print(t)
        context = {}
        context['fromStn'] = fromStation
        context['toStn'] = toStation
        context['trains'] = t
        context['journeyDate'] = j
        context['selectedClass'] = ''
        return render(request, 'show_train.html', context)
    else:
        context['Errormsg'] = "No trains found!"
        return render(request, 'index.html', context)


def check_PNR(request):
    if (request.method == 'POST'):
        context = {}
        pnr = request.POST['pnr']
        if pnr == "":
            context['errorNotFound'] = 'Enter the PNR..!'
            return render(request, 'pnr.html', context)

        td = Ticket_details.objects.filter(ticket_id=pnr)

        if td.exists():
            context['tName'] = td[0].trainNumName
            context['tNum'] = td[0].ticket_id
            context['jDate'] = td[0].journey_date
            context['sourceStn'] = td[0].fromStn
            context['destStn'] = td[0].destStn
            context['sClass'] = td[0].seating_class
            ticketJsonData = {}
            ticketJsonData['passDetails'] = json.loads(td[0].pDetails)
            context['ticketJsonData'] = ticketJsonData
            return render(request, "print_ticket.html", context)
        else:
            context['errorNotFound'] = 'PNR not exist..!'
            return render(request, 'pnr.html', context)

    else:
        return render(request, 'pnr.html', {})


def chart(request):
    return render(request, 'reservation_chart.html')


def ticket_details(request):
    return HttpResponse("ok")


def book_ticket(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':
        context = {}
        seletedClass = request.POST['seletedClass']
        trainContext = request.POST['trainContext']
        arrivalTime = request.POST['arrivalTime']
        sourceStn = request.POST['sourceStn']
        destStn = request.POST['destStn']
        jDate = request.POST['jDate']
        tFare = request.POST['tFare']
        tStatus = request.POST['tStatus']
        tCount = request.POST['tCount']

        context['seletedClass'] = seletedClass
        context['trainContext'] = trainContext
        context['arrivalTime'] = arrivalTime
        context['sourceStn'] = sourceStn
        context['destStn'] = destStn
        context['jDate'] = jDate
        context['tFare'] = tFare
        context['tStatus'] = tStatus
        context['tCount'] = tCount
        return render(request, 'book_ticket.html', context)
    else:
        return redirect('/login')


def confirm_ticket(request):
    payment = request.POST['payment']
    ticketJson = request.POST['jsonData']
    context = {}
    context['payment'] = payment
    context['ticketJsonData'] = ticketJson
    return render(request, 'payment.html', context)


def print_ticket(request):
    ticketJson = request.POST['ticketDetails']
    ##create copy of ticketJson
    copyJson = ticketJson
    ticketJsonData = json.loads(ticketJson)
    pDetails = ticketJsonData['passDetails']
    tCount = int(ticketJsonData['tCount'])
    tStatus = ticketJsonData['tStatus']
    sClass = ticketJsonData['sClass']
    newPDetails = []
    print("st", tStatus)
    print("cehck ", (tStatus.strip() == 'AVL'))
    for p in pDetails:
        if (tStatus.strip() == 'AVL'):
            p['seatNum'] = sClass + '-CNF' + str(tCount)
            p['status'] = 'Confirmed'
            tCount = tCount - 1
            # check if current available seat count ==0 then change status=waiting(WL) and start waitingCount=1
            if (tCount == 0):
                tStatus = "WL"
                tCount = 1
        else:
            p['seatNum'] = sClass + '-WL' + str(tCount)
            p['status'] = 'Waiting List'
            tCount = tCount + 1
        # add updated passenger details instance p into newPDetails list
        newPDetails.append(p)

    print("newPDetails ", newPDetails)
    ticketJsonData['passDetails'] = newPDetails

    context = {}
    context['ticketJsonData'] = ticketJsonData
    context['tNum'] = generate_ticket_number()
    for key, value in ticketJsonData.items():
        context[key] = value
        print(f'{key}: {value}')

        ## add ticket details to the database
    ticket_details = Ticket_details.objects.create(ticket_id=context['tNum'],
                                                   fromStn=context['sourceStn'], destStn=context['destStn'],
                                                   journey_date=context['jDate'].strip(),
                                                   pDetails=json.dumps(newPDetails),
                                                   seating_class=context['sClass'], trainNumName=context['tName'])

    ticket_details.save()
    parts = context['tName'].split("|")
    trainNumber = parts[0]
    # TODO: update train table for updated seats
    trains = Train.objects.filter(trainNo=trainNumber, journeyDate=context['jDate'].strip())
    if trains.exists():
        t=trains.first()
        if tStatus == 'WL':
            if sClass.strip() == 'AC':
                t.acAvailable=0
                t.acWaiting=tCount
            else:
                t.sleeperAvailable=0
                t.sleeperWaiting=tCount
        else:
            if sClass.strip() == 'AC':
                t.acAvailable=tCount
            else:
                t.sleeperAvailable=tCount
        t.save()
        print("Updated train details to ",t)
    else:
        print("train details not found for tNumber "+trainNumber+" jDate "+context['jDate'])
    return render(request, 'print_ticket.html', context)


def generate_ticket_number():
    while True:
        # Generate a random 6-digit number
        random_number = random.randint(100000, 999999)

        # Check if the number already exists in the database
        if not Ticket_details.objects.filter(ticket_id=random_number).exists():
            return random_number


def generate_pdf(request):
    # Get the HTML content of the current page
    html_content = render_to_string('template.html', request=request)

    # Configure pdfkit options (you can adjust them as needed)
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }

    # Generate PDF from HTML content
    pdf = pdfkit.from_string(html_content, False, options=options)

    # Create and return a HttpResponse with PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="your_file_name.pdf"'  # Specify the file name
    return response


def login(request):
    context = {}
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['upass']
        if uname == "" or upass == "":
            context['Errormsg'] = "Field cannot be empty"
            return render(request, 'login.html', context)

        else:
            u = authenticate(username=uname,
                             password=upass)  # is work as select qurey...when user name password not match is written none
            if u is not None:
                return redirect('/home')
            else:
                context['Errormsg'] = "Invalid username and password"
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def register(request):
    context = {}
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        if uname == "" or upass == "" or ucpass == "":
            context['Errormsg'] = "Field cannot be empty"
            return render(request, 'register.html', context)
        elif upass != ucpass:
            context['Errormsg'] = "Passwoard did not match"
            return render(request, 'register.html', context)

        else:
            try:
                u = User.objects.create(username=uname, password=upass, email=uname)
                u.set_password(upass)
                u.save()
                context['Success'] = "User added successfully"
                return redirect('/home')
            except Exception:
                context['Errormsg'] = "Username already exits"
                return render(request, 'register.html', context)

    else:
        return render(request, 'register.html')


def logout(request):
    logout(request)
    return redirect("/home")
