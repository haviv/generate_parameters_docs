# Help Desk System Parameters

**Technical Name:** HelpDeskSystemParameters

**Category:** Configuration

**Default Value:** ""

**Impact Level:** Medium

**Description:**

This configuration parameter is designed to facilitate integration with Help Desk systems, specifically targeting settings related to the FreshService platform. It allows for the customization of interactions between the Pathlock Cloud GRC platform and an organization's help desk system, enhancing the workflow of incident management and request fulfillment.

**Business Impact:**

Effective configuration of the Help Desk System Parameters can significantly improve the efficiency of issue resolution processes, streamline communication between GRC platforms and help desk systems, and enhance overall security and compliance posture by ensuring timely and precise handling of incidents and requests.

**Technical Impact when configured:**

When correctly configured, this parameter ensures secure and seamless connectivity to FreshService or similar help desk platforms using appropriate security protocols (e.g., TLS 1.2). It allows for the validation and processing of requests and incidents raised within the GRC workflow, directly impacting how quickly and effectively these are managed within the help desk system.

**Example Scenario:**

A user notices a potential compliance issue and reports it through the Pathlock platform. The Help Desk System Parameters are configured to create a ticket in the FreshService system automatically. The ticket includes all necessary information for the help desk team to assess and address the issue promptly, ensuring that the compliance risk is mitigated efficiently.

**Related Settings:**

- HelpDeskSystemPassword

**Best Practices:** configure when integrating Pathlock Cloud GRC platform with a Help Desk system such as FreshService to ensure secure and efficient incident and request management. Avoid configuring this parameter without proper understanding of the Help Desk system's API and security requirements to prevent security risks and connectivity issues.