select *  from customer_table order by group_id limit 10

do language plpgsql
$$
declare
    mysql text;
    run_time integer:=0;
    new_rk_count integer;
    last_rk_count integer:=0;
begin
    loop
        run_time = run_time + 1;
        with temp as (select account_id, min(group_id) as rk from customer_table group by account_id)
        update customer_table set group_id=rk from temp where temp.account_id=customer_table.account_id;
        with temp as (select customer_id, min(group_id) as rk from customer_table group by customer_id)
        update customer_table set group_id=rk from temp where temp.customer_id=customer_table.customer_id;
        mysql:= 'select count(distinct group_id) from customer_table';
        execute mysql into new_rk_count;
        if last_rk_count=0 or new_rk_count<last_rk_count  then
            last_rk_count = new_rk_count;
        else
            raise notice 'Quit!';
            exit;
        end if;
        raise notice 'last_group_id_count is %, new_group_id_count is %, run_time is %', last_rk_count, new_rk_count, run_time;
        raise notice '--------';
    end loop;
end;
$$;


delete from customer_table where 1=1;

select distinct(group_id) from customer_table;