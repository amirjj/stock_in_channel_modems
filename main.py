from config import OUTPUT_DIR, INPUT_DIR, OUTPUT_FILE, INPUT_FILE
from utils import *
from DA import top_assigned_modem_distributor, \
	not_registered_modems, \
	corporate_modems_as_individual


def merge_modem_report():
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

	df1_pivot = 'SERIAL_NO'
	df2_pivot = 'IMEI'

	merged_df = merge(df1, df2, df1_pivot, df2_pivot, how_to_merge)

	save_df_to_csv(merged_df, columns, output_file)


def run():
	# merge_modem_report()
	input_file = INPUT_FILE
	df = csv_to_dataframe(input_file)

	#################### Top recieved distributors ######################
	# ag = top_assigned_modem_distributor(df, 20)
	# output_file = OUTPUT_DIR.joinpath('top_assigned_modem_distributor.csv')
	# save_df_to_csv(ag, ['CUSTOMER_NAME', 'COUNT'], output_file)

	#################### Not registered count and percentage ############

	# not_registered_list = not_registered_modems(df)
	# output_file = OUTPUT_DIR.joinpath('not_registered_modems.csv')
	# save_df_to_csv(not_registered_list, ['CUSTOMER_NAME', 'NOT_REGISTERED_PERCENTAGE', 'MODEM_COUNT'], output_file)
	#################### Corporate indevidual report ####################

	# output_file = OUTPUT_DIR.joinpath('corporate_indevidual_report.csv')
	# corporate_individual_report = corporate_modems_as_individual(df)
	# save_df_to_csv(corporate_individual_report, ['CUSTOMER_NAME', 'INDIVIDUAL_COUNT', 'CORPORATE_COUNT'], output_file)



if __name__ == "__main__":
	run()

# TODO : top distributors, number and percentage of not activated yet and cross check with sold date,
# TODO : percentage of stcok in channel not registered yet
# TODO : percentage and number of indeviduals
