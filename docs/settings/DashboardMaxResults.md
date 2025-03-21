**Technical Name: DashboardMaxResults**

**Category: Reporting**

**Default Value:** 

**Impact Level: Medium**

**Description:**
The `DashboardMaxResults` parameter controls the maximum number of results displayed on dashboards within the Pathlock Cloud GRC platform. It is vital for optimizing the dashboard's performance and usability by limiting the volume of data loaded and presented to the user at any one time.

**Business Impact:**
Setting an appropriate value for `DashboardMaxResults` ensures that dashboards remain responsive and user-friendly, even when operating with large datasets. It can prevent system slowdowns and enhance the user experience by providing a concise, relevant selection of data for quicker decision-making.

**Technical Impact when configured:**
When `DashboardMaxResults` is configured, it directly influences the load time and responsiveness of dashboards by defining a threshold for the amount of data displayed. Additionally, it impacts the sorting behavior of dashboard components, as sorting may be applied based on specified columns within the dashboard's data settings.

**Example Scenario:**
Consider a scenario where an organization's compliance dashboard is set to display every available record of compliance checks. If there are thousands of records, loading the dashboard could become slow, affecting the user's ability to quickly access and analyze necessary compliance data. By configuring `DashboardMaxResults` to a sensible limit, like 100 records, the dashboard will only display the most relevant data, thereby improving load times and focusing the user's attention on the most critical information first.

**Related Settings:** 
- `DashboardSortingOrder`
- `SinglePageReview` (not directly related but impacts how single-page reviews are managed in terms of data presentation and user interaction with the application)

**Best Practices:** 
- Configure `DashboardMaxResults` to a value that balances performance with user needs for data analysis.
- Avoid setting it too high to prevent performance issues or too low where it might omit crucial data from being displayed. 

