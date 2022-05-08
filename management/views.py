from django.shortcuts import render


def dashboard(request):
	return render(request, 'admin/dashboard.html')


def total_users(request):
	return render(request, 'admin/user.html')


def add_package(request):
	return render(request, 'admin/db-add-package.html')


def active_packages(request):
	return render(request, 'admin/db-package-active.html')


def pending_packages(request):
	return render(request, 'admin/db-package-pending.html')


def expired_packages(request):
	return render(request, 'admin/db-package-expired.html')


def booking_enquiry(request):
	return render(request, 'admin/db-booking.html')


def login_view(request):
	return render(request, 'admin/login.html')