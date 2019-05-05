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


def dealer_aging_report(requests):
	query_string = "SELECT * FROM auto_sales_dealer_aging_view"


	try:
		dealer_aging_results = DealerAging.objects.raw(query_string)


		if len(dealer_aging_results) > 0:

			return render(requests, 'report_dealer_aging.html', {'dealer_agings': dealer_aging_results,
															   'reports_tab': 'active'})
		else:
			return render(requests, 'report_dealer_aging.html', {'error': 'No results found.', 'reports_tab': 'active'})
	except TopBrandsByCount.DoesNotExist:
		return render(requests, 'report_dealer_aging.html',
					  {'error': 'Oops...Something went wrong with your report.', 'reports_tab': 'active'})

def trend_reports(requests):
	query_string_year = "SELECT * FROM auto_trend_year_view"
	query_string_month = "SELECT * FROM auto_trend_month_view"
	query_string_week = "SELECT * FROM auto_trend_week_view"
	query_string_gender_income = "SELECT * FROM auto_trend_gender_income_view"

	try:
		trend_year_results = TrendYearView.objects.raw(query_string_year)
		trend_month_results = TrendMonthView.objects.raw(query_string_month)
		trend_week_results = TrendWeekView.objects.raw(query_string_week)
		trend_gender_income_results = TrendGenderIncomeView.objects.raw(query_string_gender_income)

		if len(trend_year_results) > 0 and len(trend_month_results) > 0 and len(trend_week_results) > 0\
				and len(trend_gender_income_results) > 0:

			return render(requests, 'report_sales_trends.html', {'trends_by_year': trend_year_results,
																 'trends_by_month': trend_month_results,
																 'trends_by_week': trend_week_results,
																 'trends_by_gender_income': trend_gender_income_results,
															   'reports_tab': 'active'})
		else:
			return render(requests, 'report_sales_trends.html', {'error': 'No results found.', 'reports_tab': 'active'})
	except TopBrandsByCount.DoesNotExist:
		return render(requests, 'report_sales_trends.html', {'error': 'Oops...Something went wrong with your report.',
															 'reports_tab': 'active'})
