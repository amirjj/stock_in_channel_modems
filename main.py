from config import INPUT_DIR, OUTPUT_FILE, INPUT_FILE
import pandas as pd


def save_df_to_csv(df, columns, output_file):
	"""
	:param df: DataFrame to be saved
	:param columns: columns to be saved in csv
	:param output_file: output file path
	:return: None
	"""
	df.to_csv(output_file, sep=',', columns=columns)


def merge(df1, df2, left_on, right_on, how_to_merge):
	"""
	:param df1: first dataframe to merge
	:param df2: first dataframe to merge
	:param left_on: column in df1 to reconcile with df2
	:param right_on: column in df2 to reconcile with df1
	:param how_to_merge: inner, outer, left, right join
	:return: merged dataframe
	"""
	merged_df = pd.merge(df1, df2, left_on=left_on, right_on=right_on, how=how_to_merge)
	return merged_df


def excel_to_dataframe(input_file, input_sheet):
	"""
	:param input_file: the file to fetch data from
	:param input_sheet: the sheet to fetch data from
	:return: DataFrame of the data (from file and sheet)
	"""
	df_modem_report = pd.read_excel(input_file, sheet_name=input_sheet)
	return df_modem_report


def run():
	columns = [
		'ORDER_NO', 'SITE', 'PART_NO', 'CUSTOMER_NO', 'CUSTOMER_NAME',
		'SERIAL_NO', 'IMEI', 'DATE_CREATED', 'MSISDN_V', 'PROFILE_TYPE_V',
		'CONTRACT_TYPE_V', 'MODEL_V', 'STATUS_V', 'BUNDLE_ID_V'
	]
	output_file = OUTPUT_FILE
	input_file = INPUT_FILE

	how_to_merge = 'outer'
	df1_sheet_to_merge = 'modem_report'
	df2_sheet_to_merge = 'modem_status'

	df1 = excel_to_dataframe(input_file, df1_sheet_to_merge)
	df2 = excel_to_dataframe(input_file, df2_sheet_to_merge)

	print(df1.head(10))
	df1_pivot = 'SERIAL_NO'
	df2_pivot = 'IMEI'

	merged_df = merge(df1, df2, df1_pivot, df2_pivot, how_to_merge)

	save_df_to_csv(merged_df, columns, output_file)


if __name__ == "__main__":
	# print(OUTPUT_FILE)
	# merge()
	run()
