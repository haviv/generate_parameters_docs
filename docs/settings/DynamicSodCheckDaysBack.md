# Dynamic SoD Check Days Back

**Technical Name:** DynamicSodCheckDaysBack

**Category:** Compliance

**Default Value:** N/A

**Impact Level:** High

**Description:**

The Dynamic SoD (Segregation of Duties) Check Days Back parameter is used to define the historical time frame, in days, for which the Pathlock Cloud GRC platform will check for SoD conflicts. This setting allows for a dynamic and flexible approach to audit and compliance by focusing on a specific, configurable period.

**Business Impact:**

Setting an appropriate value for this parameter directly affects the organization's ability to monitor and manage segregation of duties conflicts effectively. By allowing the configuration of a specific lookback period, organizations can tailor their SoD conflict analysis to align with internal audit cycles or specific compliance periods, leading to more focused and efficient compliance practices.

**Technical Impact when configured:**

When configured, this parameter dynamically adjusts the analysis period for SoD conflict checks performed by the system. This can have implications for system performance and the workload of compliance teams, depending on the breadth of the lookback period set.

**Example Scenario:**

For instance, an organization may set the Dynamic SoD Check Days Back parameter to 90 days ahead of an internal compliance audit to ensure that any SoD violations within the most recent fiscal quarter are identified and addressed. This focused approach allows compliance officers to concentrate their efforts on the most relevant data, facilitating more efficient resolution of compliance issues.

**Related Settings:** 

- `CommonSettings.Default.SettingsKey`
- `CommonSettings.Default.RolesRegistryNodes`

**Best Practices:** 

- **Configure when:** Preparing for audit cycles or when recent historical analysis of SoD conflicts is required to meet compliance standards. Setting this parameter according to the organization's audit cycle can help in timely preparation and compliance assurance.
  
- **Avoid when:** The system or compliance teams are not equipped to handle the volume of data or analysis that may result from a broad lookback period, as it could lead to performance issues or overwhelm the capacity of compliance teams to review and address conflicts.