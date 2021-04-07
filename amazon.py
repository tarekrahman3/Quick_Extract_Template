parent_box_xpath = '//div[@class="a-section a-spacing-medium"]'
from xPaths import *
from xPaths import xquery as path
import pandas as pd
def parse_amazon(importURLS):
	for i in importURLS:
		driver.get(i)
		WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, parent_box_xpath)))
		parents = driver.find_elements_by_xpath(parent_box_xpath)
		print(len(parents))
		for parent in parents:
			source_links.append(i)
			try:
				data_A1 = parent.find_element_by_xpath(path.x_item_1).text
			except:
				data_A1 = ""
			try:
				data_A2 =  parent.find_element_by_xpath(path.x_item_2).text
			except:
				data_A2 =  ""
			try:
				data_A3 =  parent.find_element_by_xpath(path.x_item_3).get_attribute('href')
			except:
				data_A3 =  ""
			#try:
				#data_A4 =  parent.find_element_by_xpath(path.x_item_4)
			#except:
				#data_A4 =  ""
			#try:
				#data_A5 =  parent.find_element_by_xpath(path.x_item_5)
			#except:
				#data_A5 = ""
			#data_A6 = 
			#data_A7 = 
			#data_A8 = 
			#data_A9 = 
			#data_A10 = 
			array_I.append(data_A1)
			array_II.append(data_A2)
			array_III.append(data_A3)
			print( pd.DataFrame(({
				'source_link':[i],
				'data_A1': [data_A1],
				'data_A2': [data_A2],
				'data_A3': [data_A3]
				})))
	driver.quit()
	data = {
		'source_links': source_links,
		'array_I': array_I,
		'array_II': array_II,
		'array_III': array_III
		}
	
	return data
	
	
	
	
