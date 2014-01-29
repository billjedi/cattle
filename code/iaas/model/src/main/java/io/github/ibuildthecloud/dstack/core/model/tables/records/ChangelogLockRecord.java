/**
 * This class is generated by jOOQ
 */
package io.github.ibuildthecloud.dstack.core.model.tables.records;

/**
 * This class is generated by jOOQ.
 */
@javax.annotation.Generated(value    = { "http://www.jooq.org", "3.3.0" },
                            comments = "This class is generated by jOOQ")
@java.lang.SuppressWarnings({ "all", "unchecked", "rawtypes" })
@javax.persistence.Entity
@javax.persistence.Table(name = "changelog_lock", schema = "dstack")
public class ChangelogLockRecord extends org.jooq.impl.UpdatableRecordImpl<io.github.ibuildthecloud.dstack.core.model.tables.records.ChangelogLockRecord> implements io.github.ibuildthecloud.dstack.db.jooq.utils.TableRecordJaxb, org.jooq.Record4<java.lang.Integer, java.lang.Boolean, java.util.Date, java.lang.String>, io.github.ibuildthecloud.dstack.core.model.ChangelogLock {

	private static final long serialVersionUID = -2049600450;

	/**
	 * Setter for <code>dstack.changelog_lock.ID</code>.
	 */
	@Override
	public void setId(java.lang.Integer value) {
		setValue(0, value);
	}

	/**
	 * Getter for <code>dstack.changelog_lock.ID</code>.
	 */
	@javax.persistence.Id
	@javax.persistence.Column(name = "ID", unique = true, nullable = false, precision = 10)
	@Override
	public java.lang.Integer getId() {
		return (java.lang.Integer) getValue(0);
	}

	/**
	 * Setter for <code>dstack.changelog_lock.LOCKED</code>.
	 */
	@Override
	public void setLocked(java.lang.Boolean value) {
		setValue(1, value);
	}

	/**
	 * Getter for <code>dstack.changelog_lock.LOCKED</code>.
	 */
	@javax.persistence.Column(name = "LOCKED", nullable = false, precision = 1)
	@Override
	public java.lang.Boolean getLocked() {
		return (java.lang.Boolean) getValue(1);
	}

	/**
	 * Setter for <code>dstack.changelog_lock.LOCKGRANTED</code>.
	 */
	@Override
	public void setLockgranted(java.util.Date value) {
		setValue(2, value);
	}

	/**
	 * Getter for <code>dstack.changelog_lock.LOCKGRANTED</code>.
	 */
	@javax.persistence.Column(name = "LOCKGRANTED")
	@Override
	public java.util.Date getLockgranted() {
		return (java.util.Date) getValue(2);
	}

	/**
	 * Setter for <code>dstack.changelog_lock.LOCKEDBY</code>.
	 */
	@Override
	public void setLockedby(java.lang.String value) {
		setValue(3, value);
	}

	/**
	 * Getter for <code>dstack.changelog_lock.LOCKEDBY</code>.
	 */
	@javax.persistence.Column(name = "LOCKEDBY", length = 255)
	@Override
	public java.lang.String getLockedby() {
		return (java.lang.String) getValue(3);
	}

	// -------------------------------------------------------------------------
	// Primary key information
	// -------------------------------------------------------------------------

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Record1<java.lang.Integer> key() {
		return (org.jooq.Record1) super.key();
	}

	// -------------------------------------------------------------------------
	// Record4 type implementation
	// -------------------------------------------------------------------------

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Row4<java.lang.Integer, java.lang.Boolean, java.util.Date, java.lang.String> fieldsRow() {
		return (org.jooq.Row4) super.fieldsRow();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Row4<java.lang.Integer, java.lang.Boolean, java.util.Date, java.lang.String> valuesRow() {
		return (org.jooq.Row4) super.valuesRow();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Field<java.lang.Integer> field1() {
		return io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK.ID;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Field<java.lang.Boolean> field2() {
		return io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK.LOCKED;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Field<java.util.Date> field3() {
		return io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK.LOCKGRANTED;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public org.jooq.Field<java.lang.String> field4() {
		return io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK.LOCKEDBY;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public java.lang.Integer value1() {
		return getId();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public java.lang.Boolean value2() {
		return getLocked();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public java.util.Date value3() {
		return getLockgranted();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public java.lang.String value4() {
		return getLockedby();
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public ChangelogLockRecord value1(java.lang.Integer value) {
		setId(value);
		return this;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public ChangelogLockRecord value2(java.lang.Boolean value) {
		setLocked(value);
		return this;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public ChangelogLockRecord value3(java.util.Date value) {
		setLockgranted(value);
		return this;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public ChangelogLockRecord value4(java.lang.String value) {
		setLockedby(value);
		return this;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public ChangelogLockRecord values(java.lang.Integer value1, java.lang.Boolean value2, java.util.Date value3, java.lang.String value4) {
		return this;
	}

	// -------------------------------------------------------------------------
	// FROM and INTO
	// -------------------------------------------------------------------------

	/**
	 * {@inheritDoc}
	 */
	@Override
	public void from(io.github.ibuildthecloud.dstack.core.model.ChangelogLock from) {
		setId(from.getId());
		setLocked(from.getLocked());
		setLockgranted(from.getLockgranted());
		setLockedby(from.getLockedby());
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public <E extends io.github.ibuildthecloud.dstack.core.model.ChangelogLock> E into(E into) {
		into.from(this);
		return into;
	}

	// -------------------------------------------------------------------------
	// Constructors
	// -------------------------------------------------------------------------

	/**
	 * Create a detached ChangelogLockRecord
	 */
	public ChangelogLockRecord() {
		super(io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK);
	}

	/**
	 * Create a detached, initialised ChangelogLockRecord
	 */
	public ChangelogLockRecord(java.lang.Integer id, java.lang.Boolean locked, java.util.Date lockgranted, java.lang.String lockedby) {
		super(io.github.ibuildthecloud.dstack.core.model.tables.ChangelogLockTable.CHANGELOG_LOCK);

		setValue(0, id);
		setValue(1, locked);
		setValue(2, lockgranted);
		setValue(3, lockedby);
	}
}