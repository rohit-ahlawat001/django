from django.shortcuts import render
from django.http import HttpResponse

# def show_Response(request):
#     return HttpResponse("Your responce is here dhsdlkfdsjfldjfdfj; f;asjd;sladj")


def show_Response(request):
    # Dummy data to pass to the dashboard template
    context = {
        'total_students': 150,
        'total_collected': 45000,
        'pending_fees': 12000,
        'recent_transactions': [
            {'id': 101, 'name': 'Rahul Sharma', 'amount': 5000, 'status': 'Paid', 'date': '2026-03-01'},
            {'id': 102, 'name': 'Priya Singh', 'amount': 3500, 'status': 'Pending', 'date': '2026-03-02'},
            {'id': 103, 'name': 'Amit Kumar', 'amount': 5000, 'status': 'Paid', 'date': '2026-03-04'},
        ]
    }
    return render(request, 'dashboard.html', context)
# Create your views here.
