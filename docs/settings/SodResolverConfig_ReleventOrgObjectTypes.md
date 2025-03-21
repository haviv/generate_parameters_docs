**SoD Resolver Config Relevant Org Object Types**

**Technical Name:** SodResolverConfig_ReleventOrgObjectTypes

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** This parameter is key within Pathlock's GRC platform for setting up and enforcing Segregation of Duties (SoD) policies by specifying organization object types that are relevant for SoD conflict resolution processes. It serves as a filter to focus SoD validation efforts on transactions and roles that are significant for the organization's compliance and risk management strategies.

**Business Impact:** Effective configuration of this parameter helps ensure that the organization's SoD policies are accurately enforced, reducing the risk of fraud and ensuring compliance with relevant regulations. It supports a focused approach to SoD conflict resolution by targeting only those transactions and roles that are critical to the organization's operations, thereby optimizing compliance efforts and resources.

**Technical Impact when configured:** When correctly set, this parameter determines which transactions and roles are considered by the SoD Resolver, narrowing down the scope to those identified as relevant based on the organization's specific criteria. This precision targeting aids in the efficient identification and remediation of SoD conflicts, enhancing the overall security posture and compliance level of the organization.

**Example Scenario:** In an organization where financial transactions are closely monitored for compliance with Sarbanes-Oxley Act (SOX) requirements, only roles and transactions related to financial operations may be marked as relevant. By doing so, the SoD Resolver will focus on identifying and resolving conflicts within this subset, thereby streamlining compliance efforts and minimizing unnecessary reviews of non-financial roles and transactions.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** configure when setting up SoD policies to ensure only roles and transactions critical to organizational compliance are considered. Avoid a broad or unspecific configuration that could result in an inefficient allocation of compliance resources or oversight of critical SoD conflicts.