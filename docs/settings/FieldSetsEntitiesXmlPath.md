**Technical Name:** FieldSetsEntitiesXmlPath

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The FieldSetsEntitiesXmlPath parameter specifies the XML path for entities related to field sets within the Pathlock Cloud GRC platform. It is utilized in configuring the columns and data fields for different grids and reports, ensuring that only relevant data is displayed based on the context of the user session and specific data rules.

**Business Impact:**

Proper configuration of this parameter can enhance the usability and efficiency of data presentation to end-users, leading to better decision-making processes. Misconfiguration, however, might result in irrelevant data display or missing critical information, affecting compliance, risk management, and security operations.

**Technical Impact when configured:**

When properly configured, this parameter optimizes the data fetching process for grid and report views by filtering out unnecessary fields, which can significantly improve the performance of the Pathlock Cloud GRC platform. Additionally, it ensures that sensitive or irrelevant data is not inadvertently exposed to unauthorized users.

**Examples Scenario:**

For instance, in a scenario where an organization wants to limit the financial data (like FinancialValue or Currency) displayed to certain users based on their roles or the data rules applied, configuring FieldSetsEntitiesXmlPath can help in masking or excluding such sensitive columns from the user's view, preventing unauthorized access to financial details.

**Related Settings:**

- `SmartQueryWithoutSession`
- `FieldsHeaders`

**Best Practices:** 

configure when:
- Setting up custom reports and dashboards that require specific data fields.
- Restricting sensitive or irrelevant data from being displayed to certain users.

avoid when:
- The default configuration suffices for the user's needs, and there's no specific requirement for custom data fields.