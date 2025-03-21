**Technical Name:** DBMinDate

**Category:** Configuration

**Default Value:** The specific default value isn't provided in the code references. It is determined by the CommonSettings configuration.

**Impact Level:** Medium

**Description:** DBMinDate represents the minimum allowable date parameter within the Pathlock Cloud GRC platform's database configurations. This parameter is crucial for ensuring that date-related data falls within acceptable ranges for reporting, auditing, and other data processing tasks.

**Business Impact:** Incorrectly configuring DBMinDate can lead to the exclusion of relevant historical data in reports and audits, potentially impacting compliance posture and risk assessments. Proper configuration ensures completeness and accuracy of data analysis over the intended time span.

**Technical Impact when configured:** Ensuring DBMinDate is accurately configured is essential for data integrity and operational efficiency. It acts as a baseline for valid date entries within the system, influencing data cleansing operations and preventing erroneous data processing.

**Examples Scenario:** If your organization has operational data starting from January 1, 2010, setting DBMinDate to this date ensures that any data analysis, reporting, or auditing processes will include all relevant historical data since the company's operation within the GRC platform scope.

**Related Settings:** DBMaxDate

**Best Practices:** configure when you need to establish a clear historical data boundary for reporting and compliance purposes. Avoid configuring this parameter without understanding the oldest relevant data your organization needs to retain for GRC activities.