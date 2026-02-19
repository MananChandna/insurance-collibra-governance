# Insurance Collibra Governance POC

Enterprise-style Proof of Concept simulating Insurance governance using Snowflake + Tableau + Collibra operating model.

## Architecture

CSV → Snowflake → Analytics View → Tableau → Governance Metadata

## Components

- Snowflake Warehouse
- Insurance Tables (Customer, Policy, Claims)
- Analytics View
- Tableau Dashboard
- Business Glossary
- Dataset Inventory
- Column Mapping
- Certification Logic

## Folder Guide

sql/              → All Snowflake SQL  
data_generation/ → Synthetic data generator  
csv/              → Generated datasets  
governance/       → Collibra-style metadata  
screenshots/      → Proof artifacts  

## Workflow

1. Create Snowflake warehouse/database/schema
2. Generate synthetic insurance data
3. Load CSV into Snowflake
4. Create CLAIMS_ANALYTICS view
5. Connect Tableau
6. Build Claims Overview dashboard
7. Publish via extract
8. Prepare governance metadata

## Governance Model

Business Terms:
- Policy_ID
- Claim_Amount
- Risk_Score

Certification:
Steward Review → Owner Approval → Certified Dataset

Lineage:
POLICY_TABLE + CLAIMS_TABLE → CLAIMS_ANALYTICS → Tableau Dashboard

## Interview Summary

Built Snowflake insurance warehouse, analytics views, Tableau dashboards, glossary mapping, ownership model, certification workflow, and lineage simulation.

Author: Manan Chandna
