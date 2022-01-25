select 
case
when mod(number, 2) = 0 then 'Even'
else 'Odd'
end as is_even
from numbers
