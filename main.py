from config import INPUT_DIR
import pandas as pd


def run():
	for file in INPUT_DIR.iterdir():
		print(file)

		df_modem_report = pd.read_excel('input/ALL.xlsx', sheet_name="modem_report", nrows=10)
		df_msisdn_status = pd.read_excel('input/ALL.xlsx', sheet_name="modem_status", nrows=10)

		print(df_modem_report.head(10))

		# pd.merge(df_modem_report, df_msisdn_status, on='', how='full')


if __name__ == "__main__":
	run()