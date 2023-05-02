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
	:return: DataFrame of the file (from file and sheet)
	"""
	df_modem_report = pd.read_excel(input_file, sheet_name=input_sheet)
	return df_modem_report


def csv_to_dataframe(input_file):
	"""
	:param input_file: the file to fetch data from
	:return: dataframe
	"""
	df = pd.read_csv(input_file)
	return df
