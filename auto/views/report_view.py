from django.shortcuts import render, render_to_response, get_object_or_404
from auto.models import *

def top_brands_report(requests):
	query_string = "SELECT * FROM auto_sales_counts"
	query_string2 = "SELECT * FROM auto_sales_amount"

	try:
		top_brands_by_count = TopBrandsByCount.objects.raw(query_string)
		top_brands_by_amount = TopBrandsByCount.objects.raw(query_string2)

		if len(top_brands_by_count) > 0 and len(top_brands_by_amount) > 0:

			return render(requests, 'report_top_brands.html', {'topbrandsbycount': top_brands_by_count,
															   'topbrandsbyamount': top_brands_by_amount,
															   'reports_tab': 'active'})
		else:
			return render(requests, 'report_top_brands.html', {'error': 'No results found.', 'reports_tab': 'active'})
	except TopBrandsByCount.DoesNotExist:
		return render(requests, 'report_top_brands.html', {'error': 'Oops...Something went wrong with your report.', 'reports_tab': 'active'})

def convertible_sales_report(requests):
	query_string = "SELECT * FROM auto_sales_convertible_view"


	try:
		convertible_sales_results = ConvertibleSaleMonth.objects.raw(query_string)


		if len(convertible_sales_results) > 0:

			return render(requests, 'report_convertible_sale.html', {'convertible_sales': convertible_sales_results,
															   'reports_tab': 'active'})
		else:
			return render(requests, 'report_convertible_sale.html', {'error': 'No results found.', 'reports_tab': 'active'})
	except TopBrandsByCount.DoesNotExist:
		return render(requests, 'report_convertible_sale.html',
					  {'error': 'Oops...Something went wrong with your report.', 'reports_tab': 'active'})