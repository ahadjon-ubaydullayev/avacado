from django.shortcuts import render


def home(request):
	return render(request, 'home/index.html')


def home2(request):
	return render(request, 'home/index-v2.html')


def destination(request):
	return render(request, 'home/destination.html')


def tour_packages(request):
	return render(request, 'home/tour-packages.html')


def package_offer(request):
	return render(request, 'home/package-offer.html')


def package_detail(request):
	return render(request, 'home/package-detail.html')


def about(request):
	return render(request, 'home/about.html')


def services(request):
	return render(request, 'home/service.html')


def career(request):
	return render(request, 'home/career.html')


def career_detail(request):
	return render(request, 'home/career-detail.html')


def tour_guide(request):
	return render(request, 'home/tour-guide.html')


def gallery(request):
	return render(request, 'home/gallery.html')


def single_page(request):
	return render(request, 'home/single-page.html')


def faq_page(request):
	return render(request, 'home/faq.html')



