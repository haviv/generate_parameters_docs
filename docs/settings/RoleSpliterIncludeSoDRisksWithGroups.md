# Role Splitter Include SoD Risks With Groups

**Technical Name:** RoleSpliterIncludeSoDRisksWithGroups

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This configuration parameter determines whether Separation of Duties (SoD) risks associated with user roles should be considered alongside group memberships during the role splitting process in the Pathlock Cloud GRC platform. When enabled, this setting ensures that SoD risk analysis includes not just individual roles but also the groups those roles are part of, providing a more holistic view of potential risks.

**Business Impact:**

Enabling this parameter helps organizations in mitigating risks by ensuring that SoD conflicts are identified not only within individual user roles but also across groups that those roles are part of. This is crucial for maintaining robust security and compliance standards, as it helps in preempting potential audit findings related to SoD violations and enhances the overall risk management posture of the organization.

**Technical Impact when configured:**

Upon configuration, the system will include both role-based and group-based SoD risks in its analysis during role splitting operations. This means that the algorithm responsible for determining potential SoD conflicts will take into account the collective permissions and access rights derived from both user roles and group memberships, leading to more comprehensive risk detection and mitigation strategies.

**Examples Scenario:**

- An organization is reviewing user access as part of its quarterly audit process. By having RoleSpliterIncludeSoDRisksWithGroups enabled, the GRC platform identifies a user who, through a combination of roles and group memberships, has conflicting access rights that were not previously detected. This allows the organization to address the SoD issue before it results in an audit finding.

**Related Settings:**

- `AuthorizationReviewByRolesShowNumberOfActivities`
- `AuthorizationCertificationHideIndirectRoleAssisgment`

**Best Practices:** 
- **Configure when:** you are part of an organization with complex access rights structures involving numerous roles and groups, especially in highly regulated industries where compliance with SoD policies is critical.
- **Avoid when:** your organization has a simple role and group structure, or if the performance impact of additional processing during role splitting operations outweighs the benefits of detecting SoD risks across groups.