#!/usr/bin/env bash

mongoexport --type=csv -f baseinfo.name,baseinfo.area,listdata.xxfcbj,baseinfo.phone,baseinfo.address,baseinfo.listingDate,baseinfo.legalRepresentative,baseinfo.secretaries,baseinfo.transferMode,finance.income -d neeq -c neeq_items -o 1.csv