# SoD Impact Analysis Calculator Minimum Risk Level

**Technical Name:** SoDImpactAnalysisCalculator_MinimumRiskLevel

**Category:** Risk

**Default Value:**

**Impact Level:** High

**Description:**

This parameter determines the minimum risk level for an impact analysis conducted by the SoD (Separation of Duties) Impact Analysis Calculator. It is used to filter and assess the significance of risks associated with role changes and SoD violations within the Pathlock Cloud GRC platform.

**Business Impact:**

Setting the appropriate minimum risk level helps in prioritizing risk management efforts by focusing on the most significant risks first. It aids organizations in efficiently allocating their resources towards mitigating high-priority risks, thereby enhancing overall compliance and reducing the potential for fraud or policy violations.

**Technical Impact when configured:**

Upon configuration, the system filters out the risks below the specified minimum risk level during the simulation checks for SoD violations. This ensures that only risks meeting or exceeding the set threshold are presented for review, streamlining the risk analysis process.

**Examples Scenario:**

For instance, if the minimum risk level is set to "Medium," any changes in user roles or access rights that result in risks classified as "Low" will not be included in the impact analysis reports. This allows compliance officers to concentrate on resolving or mitigating "Medium" and "High" level risks, optimizing compliance efforts.

**Related Settings:**

- `FilterOutTerminatedEmployeesFromEmployeesData`: This setting might indirectly influence the SoD impact analysis by excluding terminated employees from the data pool.

**Best Practices:** configure when you need to streamline compliance efforts by focusing on significant risks. Avoid setting the threshold too high, as this might lead to overlooking potentially harmful low-level risks.