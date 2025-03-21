# V2 Normal Records Sort Columns

**Technical Name:** V2_Normal_Records_Sort_Columns

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `V2_Normal_Records_Sort_Columns` parameter is used to specify the default columns by which records within the Pathlock Cloud GRC platform should be sorted. This configuration impacts how data is presented in various reports and user interfaces, leading to enhanced navigability and user experience.

**Business Impact:**

Configuring the default sorting columns directly affects the ease with which end users can find, analyze, and make decisions based on the data presented. Proper configuration helps in presenting the most relevant data upfront, thus reducing time spent on data analysis and enhancing operational efficiency.

**Technical Impact when configured:**

Upon configuration, the specified columns are used as the default criteria for sorting records in the UI and reports. This means that whenever a list of records is displayed, it will be ordered based on the attributes defined by this parameter unless overridden by the user manually. 

**Examples Scenario:**

For instance, in a compliance report, setting the `V2_Normal_Records_Sort_Columns` to prioritize the 'Risk Level' followed by the 'Date of Last Audit', would ensure that the highest risk items that were audited the latest would appear at the top of the report. This aids in quickly identifying areas needing immediate attention.

**Related Settings:** 

- DailyEmailFormatedFooter
- SodResolverConfiguration

**Best Practices:** 

- **Configure when** you have identified the most critical columns for decision-making in your reports and UI. Consider fields that users most frequently seek.
- **Avoid when** there is no clear hierarchy of importance among the fields or when it could lead to information overload at the forefront. Aim for simplicity and relevance.