# Odoo Technical Task Module

This module fulfills the technical task specifications provided.

## Features

### 1. Sales Credit Limit
- A custom credit limit feature has been implemented.
- It can be enabled or disabled from the Sales settings (Sales -> Configuration -> Settings).
- The `Credit Limit` field is available on the customer form under the "Sales & Purchases" tab.

### 2. "Edit Credit Limit" Access Group
- A new security group "Edit Credit Limit" (under the Sales category) is created.
- Only users belonging to this group can edit the `Credit Limit` field.
- Other users can only view the field.

### 3. `res.region` Model
- A new model `res.region` has been created with "Region Name" and "Region Code".
- A `Region` field has been added to the customer form, list, and search views.
- You can group customers by region in the search view.

## How to Use
1. Install the module.
2. Go to `Sales -> Configuration -> Settings` and enable "Enable Credit Limit on Customers".
3. Go to `Settings -> Users & Companies -> Groups` and add users to the "Edit Credit Limit" group.
4. Go to `Contacts` and create or edit a customer. You will see the `Credit Limit` and `Region` fields.
5. Go to `Contacts -> Configuration -> Regions` to create new regions.
