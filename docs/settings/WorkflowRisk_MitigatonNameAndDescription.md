# Workflow Risk Mitigation Name And Description

**Technical Name:** WorkflowRisk_MitigatonNameAndDescription

**Category:** Compliance

**Default Value:**

**Impact Level:** High

**Description:** The WorkflowRisk_MitigatonNameAndDescription parameter is designed to enable the inclusion of mitigation names and descriptions in the SoD (Separation of Duties) check step, facilitating a deeper understanding and documentation of potential risks identified during workflow processes.

**Business Impact:** Proper configuration ensures that detailed information about risk mitigations is available for auditing and compliance purposes, significantly improving the organization's ability to demonstrate thorough risk management practices to auditors and compliance regulators.

**Technical Impact when configured:** When enabled, this feature generates a detailed SoD table that includes not only the identification of potential conflicts but also comprehensive descriptions and mitigation strategies, offering a clearer insight into how identified risks are resolved or mitigated.

**Examples Scenario:** In a scenario where an organization is undergoing an internal or external audit where evidence of SoD compliance is required, having the WorkflowRisk_MitigatonNameAndDescription parameter enabled would allow for the generation of detailed tables showcasing how identified conflicts have been addressed, including the specific mitigations put in place, thus supporting the organization's compliance efforts.

**Related Settings:** `SodCheckStep_GenerateSodTableWithDescription`

**Best Practices:** 
- **Configure when:** Detailed documentation and auditing trails are necessary for compliance purposes, or when there's a need to improve upon the organization's risk management documentation and practices.
- **Avoid when:** The organization's risk management process is informal, or documentation requirements are minimal, to prevent unnecessary complexity within the workflow process.