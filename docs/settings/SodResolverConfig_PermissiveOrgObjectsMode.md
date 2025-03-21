# SoD Resolver Config Permissive Org Objects Mode

**Technical Name:** SodResolverConfig_PermissiveOrgObjectsMode

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This configuration parameter controls the behavior of the Segregation of Duties (SoD) Resolver within the Pathlock Cloud GRC platform. When enabled, it permits the inclusion of organizational objects (e.g., roles, transactions) in the SoD analysis even if these objects do not explicitly violate SoD rules, creating a more permissive environment for SoD conflict resolution.

**Business Impact:**

Enabling this mode can significantly impact how SoD conflicts are identified and resolved, potentially allowing for a broader set of roles and transactions to be considered compliant. This can result in a more flexible approach to managing SoD risks but might increase the likelihood of overlooking critical SoD violations.

**Technical Impact when configured:**

- Allows roles and transactions without direct SoD violations to be included in SoD conflict resolution processes.
- May increase the complexity of SoD analysis by including a more extensive set of organizational objects.
- Potentially reduces the number of false positives in SoD violation reports.

**Examples Scenario:**

An organization has a policy that restricts users from performing both the creation and approval of financial transactions to prevent fraud. With the Permissive Org Objects Mode enabled, roles involved in financial transactions but not directly violating the create/approve segregation rule (e.g., viewing transactions) might still be considered in the SoD analysis. This inclusion could assist in identifying indirect SoD risks or in more flexible policy enforcement where strict segregation is not always possible.

**Related Settings:**

- ApprovalGroupTypeForAuthorizationReviewFromExcel
- GenericSheetImportName

**Best Practices:** 

- Configure when seeking a more inclusive approach to SoD conflict resolution, particularly in environments where SoD violations are managed closely and flexibility in role and transaction inclusion is desired.
- Avoid when strict enforcement of SoD rules is required, or in regulatory environments where overlooking any potential SoD conflict could result in non-compliance penalties.