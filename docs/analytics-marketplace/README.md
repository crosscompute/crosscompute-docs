# Analytics Marketplace

Sell subscription access to your report, tool, widget, dashboard, form.

!!! warning

    This functionality has not been implemented yet.

## Configuration

Marketing your automations requires two steps:

1. Specify markets. Markets are other instances of the CrossCompute server where you want your automations to be listed. Markets can collect subscription revenue for your automations on your behalf and send you revenue share. The amount of revenue share is dictated by your payment configuration.
2. Deploy automations. You can deploy automations on our servers or on your servers using the open source CrossCompute framework. Use the `--market` command-line option to announce your automations to your specified markets.

Here is an example configuration with markets and payment configuration.

```yaml
---
crosscompute: 0.9.2
name: Automation X
version: 0.0.1
input:
  variables:
    - id: x
      view: number
      path: variables.dictionary
output:
  variables:
    - id: y
      view: number
      path: variables.dictionary
scripts:
  - path: run.ipynb
markets:
  - uri: https://crosscompute.net
  - uri: https://example.net
payment:
  account: EXAMPLE-NANO-ADDRESS
  period: month
  amount: 5
  currency: nano
```

Announce automations to the specified markets using the following command. This will start the production server and tell the markets that your automations are ready to run and that you can start accepting subscription payments. This does not share your code.

```bash
crosscompute --market
```
