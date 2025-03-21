# Dashboard Sorting Order

**Technical Name:** DashboardSortingOrder

**Category:** Reporting

**Default Value:** None provided

**Impact Level:** Medium

**Description:** Determines the sorting order of entries within dashboard components, such as charts or tables, to enhance data visualization and prioritization in reports.

**Business Impact:** Proper configuration ensures critical data is presented first, aiding in quicker decision-making and prioritization of compliance, risk management, and security issues.

**Technical Impact when configured:** Enables or disables sorting based on the report's specific needs, particularly affecting how data summaries are processed and presented. In the context of trending line bars, sorting might be disabled to maintain chronological data integrity.

**Examples Scenario:** An admin wishes to adjust the sorting order of compliance violation incidents reported on the dashboard to prioritize the most recent or the highest severity incidents. By adjusting the DashboardSortingOrder, they can ensure that these critical incidents are displayed at the top, making them more visible to users for immediate action.

**Related Settings:** DashboardMaxResults

**Best Practices:** Configure the DashboardSortingOrder to align with organizational priorities and reporting needs. Avoid using a non-intuitive sorting order, which may confuse users or obscure important information.