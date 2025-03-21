# Snc QOP

**Technical Name:** SncQOP

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The SncQOP parameter (Security Quality of Protection) is integral to enhancing the security of connections between the SAP system and Pathlock's GRC platform. It specifies the level of protection (integrity, authenticity, confidentiality) applied to the data exchanged, ensuring that the communication is secure and trustworthy.

**Business Impact:**

Ensuring a high level of protection for communications between SAP systems and the Pathlock platform directly impacts an organization's ability to safeguard sensitive data, comply with regulatory requirements, and mitigate risks associated with data breaches or unauthorized access.

**Technical Impact when configured:**

Configuring SncQOP with an optimal level of security ensures that data transmitted is encrypted, authenticated, and not tampered with during transit. This protects against MITM (Man-In-The-Middle) attacks, data eavesdropping, and replay attacks, thereby maintaining the integrity and confidentiality of sensitive business data.

**Examples Scenario:**

Imagine an organization that processes highly sensitive financial information between its SAP systems and the Pathlock GRC platform. By configuring SncQOP to a high level of protection, the organization can ensure that this sensitive data is securely encrypted and authenticated, preventing any unauthorized access or data leaks during transmission. 

**Related Settings:**

- RfcConfigParameters.Codepage
- RfcConfigParameters.Language

**Best Practices:** 

- Configure SncQOP to the highest level of protection supported by your organization's infrastructure to ensure the security of data in transit.
- Avoid leaving SncQOP at its default or lower protection levels in environments where sensitive data is handled or regulatory compliance dictates high security standards.