**Technical Name:** DateTimeFormats

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The DateTimeFormats parameter specifies the format used for date and time values within the Pathlock Cloud GRC platform. This setting is crucial for the accurate handling, parsing, and display of date-time values across various data sources and reports.

**Business Impact:**

Proper configuration of the DateTimeFormats parameter is essential for maintaining data integrity and ensuring compliance with global date and time representation standards. Incorrect date-time formatting can lead to misinterpretation of critical compliance data, reporting errors, and potentially non-compliance with regulatory requirements.

**Technical Impact when configured:**

When configured correctly, the DateTimeFormats parameter ensures that date and time values are consistently parsed and displayed across the platform's reporting and data extraction functionalities. It aids in the seamless integration of data from diverse sources by standardizing date-time formats, thus minimizing data processing errors and improving overall data quality.

**Examples Scenario:**

Consider a multinational corporation that needs to aggregate compliance reports from different countries, each with its own date format. By configuring the DateTimeFormats parameter to accommodate various international date formats, the platform can accurately process and display data from all sources, ensuring the reports are comprehensive and understandable, regardless of the original date format.

**Related Settings:**

- `Delimiter`: Defines a custom delimiter for CSV content, which may include date-time values.
- `SkipLines`: Configures the number of lines to skip before processing, which can be useful when extracting date-time data from CSV files with headers.

**Best Practices:** 

- Configure when: You are integrating data from sources with differing date-time formats, or when reports are generated for audiences in various locales that require specific date-time representations.
- Avoid when: The default settings already match your organization's data formats and reporting conventions, to prevent unnecessary complexity.