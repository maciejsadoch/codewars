SELECT id,
case 
when mod(base, factor) = 0 then true
else false
end as res
FROM kata
