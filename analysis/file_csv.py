#! /usr/bin/env python3
# coding: utf-8

import os
import pandas as pd
import matplotlib.pyplot as plt


class SetOfMediaChannel:
	ALL_REGISTERED_MEDIA = [] # This is a class attribute

	def __init__(self, name, year):
		self.name = name
		self.year = year

	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, sep=",")
		self.dataframe = self.dataframe.loc[self.dataframe['year'] == self.year]
		media = self.dataframe["channel_name"].dropna().values
		self._register_media(media)

	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe
		media = self.dataframe["channel_name"].dropna().values
		self._register_media(media)

	@classmethod
	def _register_media(cl, media):
		cl.ALL_REGISTERED_MEDIA = cl._group_two_lists_of_media(cl.ALL_REGISTERED_MEDIA, list(media))

	@classmethod
	def get_all_registered_media(cl):
		return cl.ALL_REGISTERED_MEDIA

	@staticmethod
	def _group_two_lists_of_media(original, new):
		return list(set(original + new)) # This line drop duplicates in the list 'original + new'

	def display_chart(self):
		data = self.dataframe
		women_expression_rate = data['women_expression_rate'].sum() / len(data)
		man_expression_rate = 100 - women_expression_rate
		proportions = [women_expression_rate, man_expression_rate]
		labels = ["women_expression_rate", "man_expression_rate"]

		fig, ax = plt.subplots()
		ax.axis("equal")
		ax.pie(
		        proportions,
		        labels=labels,
		        autopct="%1.1f%%"
		        )
		plt.title("{} (year : {})".format(self.name, self.year))
		plt.show()


	def split_by_channel(self, year):
		result = {}
		data = self.dataframe

		# These 2 syntaxes are equivalent : data.channel_name and data['channel_name']
		all_channels = data["channel_name"].dropna().unique()

		for channel in all_channels:
		    data_subset = data[data.channel_name == channel]
		    subset = SetOfMediaChannel('"{}"'.format(channel), year)
		    subset.data_from_dataframe(data_subset)
		    result[channel] = subset
		return result

	def split_by_type(self, year):
		result = {}
		data = self.dataframe

		# These 2 syntaxes are equivalent : data.media_type and data['media_type']
		all_media_types = data["media_type"].dropna().unique()

		for media_type in all_media_types:
			data_subset = data[data.media_type == media_type]
			subset = SetOfMediaChannel('"{}"'.format(media_type), year)
			subset.data_from_dataframe(data_subset)
			result[media_type] = subset
		return result

def launch_analysis(data_file, year, bychannel = False, bytype = False):

	somc = SetOfMediaChannel("All media channels", year)
	somc.data_from_csv(os.path.join("data",data_file))
	for i in somc:
		print(i)
	#somc.display_chart()

	if bychannel:
		for channel, s in somc.split_by_channel(year).items():
			pass
			#s.display_chart()

	if bytype:
		for media_type, s in somc.split_by_type(year).items():
			pass
			#s.display_chart()



if __name__ == "__main__":
	launch_analysis('data.csv')
