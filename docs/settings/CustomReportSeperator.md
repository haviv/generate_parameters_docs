# Custom Report Separator

**Technical Name:** CustomReportSeperator

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Custom Report Separator parameter allows users to specify a character or string used to separate fields in report exports. This is particularly useful for tailoring the format of the output files for compatibility with various external systems or preferences in data handling.

**Business Impact:**

The choice of separator has a direct impact on data analysis and processing efficiency. An incorrect separator can lead to data misinterpretation, challenges in data import into other systems, and overall reduced data usability. Correctly configuring this parameter ensures seamless data export/import workflows, enhancing productivity and data integrity across systems.

**Technical Impact when configured:**

Proper configuration of the Custom Report Separator ensures that exported report data is formatted correctly for use by downstream systems, such as ERP, HRIS, or custom internal systems. It affects how data is parsed and understood by both humans and machines, potentially influencing data processing pipelines and analytics platforms.

**Examples Scenario:**

For instance, if an organization uses a comma (,) as a standard field separator in their systems, but their exported reports use a semicolon (;), this mismatch can cause issues when importing data. Configuring the Custom Report Separator to use a comma can resolve such integration issues, ensuring smooth data flow between Pathlock Cloud GRC and external systems.

**Related Settings:** 

- `SmartSearchKey`: Might influence how searches and filters are applied before report generation, hence affecting the data that would be separated by the Custom Report Separator.

**Best Practices:** 

- **Configure when:** You need to match the report output format with the expectations of downstream systems or standards within your organization.
  
- **Avoid when:** Default settings already satisfy your organizational and technical requirements for report formatting.