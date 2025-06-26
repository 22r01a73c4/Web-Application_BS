from django.shortcuts import render

def dashboard_view(request):
    context = {
        'user': 'Vishal',
        'ipo_stats': {
            'gain': 20,
            'loss': 9,
            'total': 30
        },
        'main_board_ipo': {
            'upcoming': 15,
            'new_listed': 25,
            'ongoing': 2
        },
        'quick_links': [
            {'name': 'NSE India', 'url': '#'},
            {'name': 'BSE India', 'url': '#'},
            {'name': 'SEBI', 'url': '#'},
            {'name': 'Money Control', 'url': '#'},
        ]
    }
    return render(request, 'dashboard.html', context)
