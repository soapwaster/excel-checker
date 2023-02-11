
# Excel checker

![BT](https://github.com/soapwaster/excel-checker/actions/workflows/main.yaml/badge.svg)

With this project it's possible to run user-defined validation checks on excel files (including sheets, rows, columns and cells).
# Gettin started
## Download the repo
Download the repo and create a folder called `custom-checks` under `res`. 
## Your first check
	The first step is create custom checks for your file. Let's say you are a car dealer and have an excel file with information related to cars that just arrived in your shop. You want to make sure that no cars produced after 2000 has more than 120.000 kms and that there are no cars with more than 3 previous owners. We'll call these checks *R_LowMileage* and *C_Owners* respectively. Let's define them. For brevity we'll only write R_LowMileage. It is a row check as it checks the content of rows.
Create a python file called R_LowMileage.py and place is under `res/custom-checks`

    class  R_LowMileage(RowCheck):
		def  _code(self):
			return  "R_LowMileage"
			
		def  _columns_checked(self):
			return ["D","E"]

		# Code to execute
		# returns self.correct
		def  perform(self):	
			self.correct = True
			
			year = self.row.getColInRow(4)
			kms = self.row.getColInRow(5)
			
			if year > 2000 and kms > 120000:
				self.correct = False

			return  self.correct
## Setting up the configuration file
Once you have your checks, it is time to declare where you want to execute them. To do so, create a yaml file called `config_dealer.yaml` and place is under `res/custom-checks`

	Sheets:
	  [
	    {
	      name: New,
	      Rows: [{ from: 8, to: 10, checks: [R_LowMileage] }],
	      Columns: [{ from: 6, to: 6, checks: [C_Owner] }],
	    },
	  ]