# SoD Resolver Max No Of Combinations To Show

**Technical Name:** SodResolver_MaxNoOfCombinationsToShow

**Category:** SoD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the maximum number of violation combinations that will be displayed to the user. It is aimed at optimizing the user experience by limiting the quantity of data to a manageable level, focusing on the most relevant information.

**Business Impact:**

Setting an appropriate value for this parameter is crucial for performance and usability. A value too high may overwhelm users with excessive information, making it difficult to identify crucial violations, whereas a value too low might hide significant security risks.

**Technical Impact when configured:**

Proper configuration ensures that only the most pertinent SoD violation combinations are shown, enhancing usability and allowing for efficient identification and resolution of critical compliance issues.

**Examples Scenario:**

- **Enhancing Performance:** In a scenario where the system detects hundreds of violation combinations, this setting can be adjusted to show only the top 50, ensuring that the application remains responsive and the data manageable.
- **Focusing on Relevance:** When reviewing violations post-upgrade or implementation, setting this parameter to a lower number can help focus on the most significant issues first.

**Related Settings:**

- `CheckDynamicSoDOnLogRecordsWithChangesOnly`

**Best Practices:** 

- **Configure when:** Adjust the value based on the average number of violations your organization encounters during a typical audit cycle for a focused and efficient review process.
- **Avoid when:** Do not set this value too low in environments where comprehensive SoD violation review is critical, to ensure no significant risk is overlooked.