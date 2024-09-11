# Budgeting app
Project management document

## Basic structure of the data

### Cashflow registering
* The basic unit of data is a transaction - financial event described with amount, date, category, group and description
* The group is a high level description of the transaction purpose - cost, investment, free spending, savings, income. It consists of a code, name and description
* The category is linked to the group (many categories to one group). Category consists of code, name, description and group code, and active flag (it does not have to be used, but we won't delete any in principle)

### Cashflow planning
* The basic unit is category quota for a month. It consists of category code, month (date, but only month and year are significant), and planned amount and a comment (perhaps even a long one, to accomadate additional informations for a given time pariod)

## User stories

### Main - top priority

#### App opening and navigation
As a user I want to be able to open main page and navigate to relevant pages using visible links.

#### Groups management
As a user I want to be able to 
* view existing groups
* add new groups
* modify existing groups

#### Categories management
As a user I want to be able to 
* view existing categories
* add new categories
* modify existing categories

#### Budgeting - planning a month
As a user I want to be able create and edit a budget for a month using a simple form, which will allow me to update all of the categories for a given time period at once. 

_This should be integrated within the viewing page - on clicking an edit button, the editable fields with new amounts (quotas) shoud be visible next to aggregated spending and current plan, as well as with the comment fields next to them_

#### Budgeting - viewing a month
As a user I want to be able to view a budget for a month using a view, which will also provide me a summed up spending for each categories and groups.

#### Transaction recording
As a user I want to be able to enter multiple transactions at once using a readable form.

### Backlog
#### Copying plan from a different month
As a user I want to be able to copy planned month into a different one, but I want to be asked twice for it not to override changes by mistake

#### Exporting the plan in excel spreadsheet
As a user I want to export the data for a given month in an excel format - one spreadsheet with two workbooks, one for the budget allocations and spending, second one for transaction list

#### View an extended period of months
As a user I want to have a dashboard on which I would be able to create cumulated and detailed reports for multiple months, to either see how the trends look like through time