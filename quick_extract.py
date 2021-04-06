from xPaths import xquery as path
from xPaths import *

df = pd.read_csv('import_file.csv', header=0)
importURLS = df.links.to_list()

for i in importURLS:
	source_links.append(i)
	driver.get(i)
	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, path.x_item_1)))
	try:
		data_A1 = driver.find_element_by_xpath(path.x_item_1).get_attribute('href')
	except:
		data_A1 = ""
	#try:
		#data_A2 =  driver.find_element_by_xpath(path.x_item_2)
	#except:
		#data_A2 =  driver.find_element_by_xpath(path.x_item_3)
	#try:
		#data_A3 =  driver.find_element_by_xpath(path.x_item_4)
	#except:
		#data_A3 =  driver.find_element_by_xpath(path.x_item_5)
	#try:
		#data_A4 =  driver.find_element_by_xpath(path.x_item_6)
	#except:
		#data_A4 =  driver.find_element_by_xpath(path.x_item_7)
	#try:
		#data_A5 =  driver.find_element_by_xpath(path.x_item_8)
	#except:
		#data_A5 =  driver.find_element_by_xpath(path.x_item_9)
	#data_A6 = 
	#data_A7 = 
	#data_A8 = 
	#data_A9 = 
	#data_A10 = 
	array_I.append(data_A1)
	print( pd.DataFrame({
		'source_link':[i],
		'data_A1': [data_A1]
		}))

data = {
	'source_links': source_links,
	'array_I': array_I
	}

df = pd.DataFrame (data, columns = ['source_links', 'array_I'])
print( df)
df.to_csv(r'export_data.csv', index = False, header=True)
