# Campaign Name Date Format

**Technical Name:** CampaignNameDateFormat

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The CampaignNameDateFormat parameter is designed to specify the format used for date representation within campaign names. This setting is crucial for ensuring that campaign names are consistently formatted, promoting better organization and easier identification of campaigns over time.

**Business Impact:**

Correctly setting the CampaignNameDateFormat impacts how easily users can identify and access different authorization campaigns, especially when sorting or searching through historical data. A standardized date format in campaign names enhances usability and efficiency in managing campaigns.

**Technical Impact when configured:**

Configuring the CampaignNameDateFormat parameter ensures that all new campaigns follow a consistent naming convention that includes the date in the preferred format. This consistency aids in automation processes, reporting, and data management, as it avoids confusion that may arise from varying date formats.

**Examples Scenario:**

Scenario: An organization wants to streamline its campaign management by making it easier to identify campaigns based on their start dates. By configuring the CampaignNameDateFormat to "YYYY-MM-DD", all campaigns will follow a uniform naming convention that includes the precise start date, facilitating quick identification and sorting.

**Related Settings:**

- DefaultCcmCurrency

**Best Practices:** configure when setting up the system to ensure consistency from the start; avoid when there is already an established, different date format convention in use to prevent confusion.