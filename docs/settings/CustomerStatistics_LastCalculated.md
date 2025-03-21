# Customer Statistics Last Calculated

**Technical Name:** CustomerStatistics_LastCalculated

**Category:** Reporting

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

The `CustomerStatistics_LastCalculated` parameter is used to track the last time customer-related statistics were calculated within the Pathlock Cloud GRC platform. This parameter ensures that the data presented in reports is up-to-date and reflects the most recent activities within the system.

**Business Impact:**

Understanding when customer statistics were last calculated is crucial for organizations to ensure they are making decisions based on the latest data. It affects reporting accuracy, which in turn can influence strategic business decisions, risk assessment, and compliance status. 

**Technical Impact when configured:**

Configuring the `CustomerStatistics_LastCalculated` parameter directly influences the recency of the data used in generating reports and analytics. When updated, it ensures that the customer statistics within the dashboard and reports are accurate as of the last calculation date.

**Examples Scenario:**

A company performs a quarterly review of its security posture and compliance status across its customer base. By reviewing the `CustomerStatistics_LastCalculated` parameter, they can confirm that the statistics presented in the dashboard were calculated after the most recent quarter ended, ensuring that the review is based on current and relevant data.

**Related Settings:**

- `CustomerStatistics_Every`

**Best Practices:** 

- **Configure when:** Regular updates to customer statistics are required to maintain up-to-date reporting and analytical capabilities.
  
- **Avoid when:** Frequent recalculations may not be necessary if your customer base and their associated data do not change often, or it might lead to unnecessary processing load on the system.