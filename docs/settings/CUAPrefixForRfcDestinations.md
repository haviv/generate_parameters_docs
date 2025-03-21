# Central User Administration Prefix For Rfc Destinations

**Technical Name:** CUAPrefixForRfcDestinations

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CUAPrefixForRfcDestinations` parameter defines the prefix used for SAP RFC (Remote Function Call) destinations that are managed under Central User Administration (CUA) in the SAP system. This setting enables the Pathlock Cloud GRC platform to correctly identify and work with those RFC destinations that are part of the CUA landscape, aiding in the seamless management of user permissions and compliance.

**Business Impact:**

Correct configuration of this parameter ensures efficient and secure communication between SAP systems managed under Central User Administration. It helps maintain compliance by ensuring that only authorized RFC calls are made, contributes to the integrity of system-to-system communications, and facilitates the centralized management of user permissions and system accesses.

**Technical Impact when configured:**

When properly configured, `CUAPrefixForRfcDestinations` allows for the accurate identification and filtering of RFC destinations that fall under CUA, ensuring that operations related to security, risk, compliance, and user management are correctly applied to these endpoints. It directly impacts how the Pathlock platform interacts with SAP systems for activities like data fetching, permission synchronization, and compliance checks.

**Examples Scenario:**

A company has multiple SAP systems with RFC destinations, some of which are managed under Central User Administration (CUA). By setting `CUAPrefixForRfcDestinations` to the appropriate prefix used by the company for its CUA-managed systems, Pathlock is able to distinguish these RFC destinations from others. This enables specific compliance checks and security policies to be applied only to those RFC destinations, helping maintain a secure and compliant SAP landscape.

**Related Settings:**

- `SapUserName`
- `DestSystem`

**Best Practices:** 

- **Configure when**: There is a need to differentiate and specifically manage RFC destinations that fall under Central User Administration within the Pathlock platform.
  
- **Avoid when**: All RFC destinations across the SAP landscape do not require distinct management or identification under Central User Administration contexts.