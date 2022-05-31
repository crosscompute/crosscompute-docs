# Analytics Marketplace

Sell subscription access to your report, tool, widget, dashboard, form.

!!! warning

    This functionality has not been implemented yet.

## Configuration

Marketing automations to your peers requires two steps:

1. Specify peers. Peers are other instances of the CrossCompute server where you want your automations to be listed. Peers can collect subscription revenue for your automations on your behalf and send you revenue share. The amount of revenue share is dictated by your payment configuration.
2. Deploy automations. You can deploy automations on our servers or on your servers using the open source CrossCompute framework. Use the `market` command-line option to market your automations to your specified peers.

Here is an example configuration with peers and payment configuration.

```yaml
---
crosscompute: 0.9.2
name: Automation X
version: 0.0.1
peers:
  - uri: https://crosscompute.net
  - uri: https://example.net
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
payment:
  account: EXAMPLE-NANO-ADDRESS
  period: month
  amount: 5
  currency: nano
```

Market automations to the specified peers using the following command. This will start the production server and tell the peers that your automations are ready to run and that you can start accepting subscription payments.

```bash
crosscompute --market
```
