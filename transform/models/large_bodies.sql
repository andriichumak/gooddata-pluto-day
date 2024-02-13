with source_data as (
    select
        l1.ID,
        l1.BODYTYPE as TYPE,
        l1.ENGLISHNAME as NAME,
        l1.GRAVITY,
        l1.DENSITY,
        l1.AVGTEMP as AVG_TEMP,
        coalesce(try_to_date(l1.DISCOVERYDATE, 'DD/MM/YYYY'), try_to_date(l1.DISCOVERYDATE, 'YYYY'), try_to_date(l1.DISCOVERYDATE, '??/MM/YYYY')) as DISCOVERY_DATE,
        l1.DISCOVEREDBY as DISCOVERED_BY,
        l1.MEANRADIUS as MEAN_RADIUS,
        l1.SEMIMAJORAXIS * 6.68459e-9 as SEMIMAJOR_ORBIT,
        coalesce(l1.MASS_MASSVALUE, 0) * pow(10, coalesce(l1.MASS_MASSEXPONENT, 6) - 6) as MASS,
        coalesce(l1.VOL_VOLVALUE, 0) * pow(10, coalesce(l1.VOL_VOLEXPONENT, 0)) as VOLUME,
        coalesce(l2.ENGLISHNAME, l1.ENGLISHNAME) as PLANETARY_SYSTEM
    FROM ANDY.PLUTO.BODIES AS l1
    LEFT JOIN ANDY.PLUTO.BODIES AS l2 ON l1.AROUNDPLANET_PLANET = l2.id
    WHERE
        l1.BODYTYPE IN ('Star', 'Planet', 'Dwarf Planet', 'Moon')
)

select *
from source_data
