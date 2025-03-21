# External Data Column Decimal Precision

**Technical Name:** ExternalDataColumnDecimalPrecision

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This setting controls the precision of decimal values in external data columns when data is imported into the Pathlock platform. Adjusting this setting ensures that decimal data aligns with an organization’s specific data accuracy requirements.

**Business Impact:** Proper configuration of this parameter is crucial for financial computations, reporting, and analysis, where decimal precision can significantly affect financial totals, risk assessments, and compliance status. Incorrect precision settings may lead to data inaccuracies, affecting business decisions and reporting integrity.

**Technical Impact: when configured** Adjusting the External Data Column Decimal Precision parameter directly impacts how decimal data is recorded, displayed, and used in calculations within the Pathlock platform. This precision level affects data synchronization, reporting, and any process relying on decimal column data, ensuring that numerical data conforms to organizational standards and expectations.

**Examples Scenario:** If an organization must comply with financial reporting standards requiring decimal precision to two places for currency values, configuring this parameter accurately will ensure that financial data imported into Pathlock reflects this requirement, thereby maintaining compliance and ensuring the integrity of financial reports.

**Related Settings:**

**Best Practices:** configure when importing decimal data that needs to adhere to specific precision requirements, avoid when default system settings meet organizational data precision needs.