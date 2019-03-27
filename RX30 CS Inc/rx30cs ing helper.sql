select * from config.newDetails where Rkey= 5 order by TableName;

select * from config.newLog ;

select * from config.newSources ;

select L.Rkey Rkey,L.RunID RunID, L.IngTargetFolder TargetFolder, 
L.IngStatus IngStatus, L.StagingStatus StgStatus,D.TableId as TableId, 
concat('rx30CS-',S.TargetTable) as IngTableName, S.StgTableName as StgTableName, D.TableName 
from config.newLog L
join config.newDetails D on L.Rkey = D.Rkey
join config.newSources S on D.TableID = S.RowKey 
where D.Rkey=(select max(Rkey) from config.newlog ) 
