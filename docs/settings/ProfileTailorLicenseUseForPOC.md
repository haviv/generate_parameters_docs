# Pathlock License Use For POC

**Technical Name:** ProfileTailorLicenseUseForPOC

**Category:** Configuration

**Default Value:** None provided

**Impact Level:** Medium

**Description:**

This parameter controls whether a Proof of Concept (POC) license is utilized within the Pathlock GRC platform specifically for ProfileTailor. It allows for the activation and validation of a product key under a POC agreement, affecting how the system checks and acknowledges the use of licenses during the POC phase.

**Business Impact:**

Using the POC license can significantly impact the decision-making process for potential long-term adoption by allowing stakeholders to evaluate the platform's capabilities in a real-world environment without committing to a full license upfront. 

**Technical Impact when configured:**

When configured, this parameter enables the use of a temporary license for evaluating the product's full functionality. It alters the licensing validation process to accept POC licenses, which may come with specific limitations or terms different from standard licensing.

**Examples Scenario:**

- A company is considering Pathlock for their GRC needs but wants to trial its full suite of features. By using the ProfileTailorLicenseUseForPOC parameter, they can enable a POC license that allows them to fully test the product before making a purchase decision.

**Related Settings:** ProfileTailorLicenseUseSubscriptionBasedLicense

**Best Practices:** configure when evaluating the Pathlock GRC platform to understand its capabilities and fit for your organization. Avoid configuring this for long-term production usage, as full licensing provides ongoing support and updates.