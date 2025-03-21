# Max Records For Excel Sheet

**Technical Name:** MaxRecordsForExcelSheet

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `MaxRecordsForExcelSheet` parameter specifies the maximum number of records that can be exported to a single Excel sheet within the Pathlock Cloud GRC platform. It is used to control the volume of data being exported to ensure optimal performance and manageability of Excel reports.

**Business Impact:**

Setting an appropriate limit for this parameter helps in maintaining a balance between report detail and performance. It prevents generating Excel sheets that are too large to be opened or processed efficiently, enhancing user experience by ensuring reports are manageable and align with users' needs for analysis and decision-making.

**Technical Impact when configured:**

Configuring `MaxRecordsForExcelSheet` affects how data is chunked and written to Excel files. If the number of records exceeds the set maximum, the data may be split across multiple sheets or files, influencing the way reports are structured and how users interact with them.

**Examples Scenario:**

A compliance officer needs to export a report detailing user access rights across all departments. If the total records exceed the `MaxRecordsForExcelSheet`, the report will be broken down into multiple sheets, ensuring that each sheet can be accessed and analyzed without performance issues.

**Related Settings:**

- `MaxRecordsForExcelSheetBuffer`

**Best Practices:** configure when a report is expected to generate a large amount of data to prevent performance degradation. Avoid setting this value too low to ensure comprehensive data coverage in reports.