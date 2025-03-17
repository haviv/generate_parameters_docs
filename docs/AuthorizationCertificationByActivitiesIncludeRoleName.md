# Authorization Certification By Activities Include Role Name

**Technical Name:** AuthorizationCertificationByActivitiesIncludeRoleName

**Category:** Audit

**Default Value:** {0}

**Impact Level:** High

**Description:** 
This parameter configures the inclusion of role names in authorization certifications when reviewing activities. It is utilized to enhance the visibility and traceability of roles associated with particular activities within the Pathlock Cloud GRC platform.

**Business Impact:** 
Enabling this feature can greatly assist in comprehending the scope and responsibilities of roles within an organization, increasing transparency in the audit and compliance processes. It aids in identifying potentially over-permissioned roles or misalignments between roles and activities, reducing security risks and ensuring compliance with internal policies and external regulations.

**Technical Impact when configured:**
When this parameter is configured to include role names in the authorization certification reviews, it enriches the data provided during audits and compliance checks. It allows for a more detailed analysis and understanding of the access rights and limitations associated with each role, streamlining the certification process by providing clearer insights into authorization structures.

**Example Scenario:**
- A compliance officer is reviewing the access rights of employees in sensitive departments. By enabling this parameter, the officer can see not only the activities that individual members are authorized to perform but also the roles associated with these activities. This detail makes it easier to verify that access rights are in compliance with the principle of least privilege and regulatory requirements.

**Related Settings:**
- ActivityDetailsVisibility
- RoleCertificationDetails

**Applicable Workflow Actions:**
- Generate Authorization Review Report
- Initiate Authorization Certification Process
- Review Authorization Certifications

**Best Practices:** 
- **Configure when:** 
   - You require detailed auditing and review of authorization certifications.
   - It is critical to understand the mapping between roles and activities for security and compliance reasons.
- **Avoid when:** 
   - Simplicity is preferred over detail in certification reports, or when the inclusion of role names might create unnecessary complexity or data privacy concerns.

**Context:**
This parameter plays a crucial role in enhancing the effectiveness of audits, compliance checks, and general security governance within the Pathlock Cloud GRC platform by providing an additional layer of detail during the review of authorization certifications by activities. Its configuration can be tailored to meet the specific needs of an organization's security and compliance policies.