# Query Designer Display Timeout

**Technical Name:** QueryDesginerDisplayTimout

**Category:** Configuration

**Default Value:** 600

**Impact Level:** Medium

**Description:**

The `QueryDesginerDisplayTimout` parameter defines the timeout threshold in seconds for displaying results in the Query Designer interface within the Pathlock Cloud GRC platform. This setting is particularly relevant when running complex queries that may take a significant amount of time to process and render.

**Business Impact:**

Adequately configuring this parameter ensures that users can effectively execute and view results of complex queries without unexpected timeouts, thus supporting efficient and uninterrupted risk analysis, compliance activities, and reporting workflows. Misconfiguring this parameter may lead to a poor user experience by either causing premature query cancellations or excessively long wait times.

**Technical Impact when configured:**

- **Correct Setting**: Enhances the usability of the Query Designer by preventing premature timeouts, ensuring users can complete their intended actions without interruption.
- **Incorrect Setting**: May cause the Query Designer to time out prematurely for complex queries that require more time to execute, or conversely, may lead to unnecessary waits for query completion, affecting user productivity.

**Examples Scenario:**

A compliance officer needs to run a complex query to identify potential SOD (Segregation of Duties) violations across all roles within the organization. Setting the `QueryDesginerDisplayTimout` to an appropriately high value ensures that the query completes and the results are displayed, thus aiding in the timely identification and mitigation of compliance risks.

**Related Settings:** QueryDesginerExportToExcelTimout

**Best Practices:** 
- **Configure when** running complex queries that are essential for compliance and risk management activities, to ensure complete results are rendered without interruption.
- **Avoid when** default settings meet the organization's operational requirements for query execution and display times, to maintain system performance and user productivity.