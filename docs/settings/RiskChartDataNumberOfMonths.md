# Number of months to display on Risk Chart

**Technical Name:** RiskChartDataNumberOfMonths

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the duration in months for which data is displayed on the Risk Charts within the Pathlock Cloud GRC platform. It allows users to customize the time frame of risks visualization to better align with their audit and review cycles.

**Business Impact:**

Setting the appropriate number of months impacts the organization's ability to monitor and review risks over a specific period efficiently. This can aid in identifying trends, preparing for audits, and ensuring compliance with various regulatory requirements.

**Technical Impact when configured:**

Configuring this parameter affects the Risk Charts by limiting or expanding the historical data presented. It helps in focusing the analysis on a specified period, which can be crucial for identifying patterns or issues within a particular timeframe. 

**Examples Scenario:**

If an organization has a quarterly audit process, setting this parameter to '3' will ensure that the Risk Charts align with these audits, providing relevant data for the auditors and internal review teams to assess.

**Related Settings:** 

- `Image_Background`: This setting may be related in terms of customizing the aesthetic aspects of reports including Risk Charts.
- `Image_LoginLogo`: Although primarily affecting login page branding, it indicates the level of UI customization available, including reports display.

**Best Practices:** 

- **Configure when:** There is a need to align risk reporting with specific business cycles such as audit schedules, fiscal quarters, or project timelines.
- **Avoid when:** There is no clear requirement for a specific reporting period, or when data for extended periods is necessary for comprehensive risk analysis and decision-making.