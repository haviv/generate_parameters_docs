**Read Change Document When Detecting Dynamic SoD Violation Min Level**

**Technical Name:** ReadChangeDocumentWhenDetectingDynamicSodViolationMinLevel

**Category:** Risk

**Default Value:** False

**Impact Level:** Medium

**Description:** Determines whether to read change documents for mitigated entities upon detecting a minimum level of dynamic Separation of Duties (SoD) violations. Useful for organizations needing to enforce and review mitigations in dynamic, high-volume transaction environments.

**Business Impact:** Enables tighter control and oversight over dynamic SoD violations by providing visibility into change documents for entities with mitigated risk. This helps ensure compliance with regulatory requirements and internal policies by automating the oversight of mitigations and their related changes.

**Technical Impact when configured:** Activating this setting will cause the system to evaluate and potentially access change documents for entities such as employees or entity objects when they are involved in mitigated dynamic SoD violations. This can increase awareness and control over changes that might influence SoD risks but may incur additional processing overhead.

**Examples Scenario:** If a company has defined dynamic SoD rules and avoids conflicts between critical transactions, enabling this setting ensures that any changes to mitigations—for example, role changes in an employee's profile affecting SoD—are documented and retrievable. This is particularly important in environments where transaction integrity and audit trails are vital for compliance.

**Related Settings:** 

- *ExcludeEmptyActivityModes*: Ensures that activities without meaningful actions are not considered in audits or compliance checks.

**Best Practices:** 

- **Configure when:** There's a need for detailed audit trails and oversight for mitigations applied to dynamic SoD violations. Particularly useful for environments subject to stringent compliance requirements.
  
- **Avoid when:** System performance and overhead are critical concerns, and the additional information provided by accessing change documents does not justify the potential impact on system resources.